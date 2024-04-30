<script>
  import { goto } from "$app/navigation";

  export let image = "";
  export let name = "";
  export const coinId = "";
  export const cryptoId = ""
  async function navigate() {
    // console.log(name,coinId,cryptoId)
    goto(`/top-pick/${name.toLowerCase()}`); // Pass coin data as context
  }
</script>

<div class="card w-60 bg-base-100 shadow w-xl">
  <figure class="bg-secondary py-5 w-px-100 h-px-100">
    <img class="" src={image} alt={name + "_Logo"} />
  </figure>
  <div class="card-body">
    <h2 class="card-title">{name}</h2>
    <!-- <div class="text-lg">Price: {price}</div> -->
    <div class="card-actions justify-end">
      <button class="btn btn-primary" on:click={navigate}>Buy Now</button>
    </div>
  </div>
</div>
