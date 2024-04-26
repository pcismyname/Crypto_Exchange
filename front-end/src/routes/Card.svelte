<script>
  import { goto } from "$app/navigation";

  export let image = "";
  export let name = "";
  export let price = "";
  export let coinId = "btc"; // Add coinId prop


  async function navigate() {
    // Optional data loading before navigation (if needed)
    // const coinData = await load({ fetch: async () => {
    //   // Fetch coin details from an API or local data
    //   const response = await fetch(`/api/coins/${coinId}`);
    //   return response.json();
    // }});
    console.log('btc');
    goto(`/top-pick/${coinId}`); // Pass coin data as context
  }
</script>

<div class="card w-60 bg-base-100 shadow w-xl">
  <figure class="bg-secondary py-5 w-px-100 h-px-100">
    <img class="" src={image} alt={name + "Logo"} />
  </figure>
  <div class="card-body">
    <h2 class="card-title">{name}</h2>
    <div class="text-lg">Price: {price}</div>
    <div class="card-actions justify-end">
      <button class="btn btn-primary" on:click={navigate}>Buy Now</button>
    </div>
  </div>
</div>
