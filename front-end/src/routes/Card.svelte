<script>
    import { goto } from '$app/navigation';
    export let image = "";
    export let name = "";
    export let price = "";
    export let targetUrl = "#";

    function navigate() {
        goto(targetUrl);
    }
  </script>
  
    <!-- <div class="flex flex-col min-w-20 max-w-60 min-h-75 items-center justify-center bg-secondary">
      <img class="rounded-full h-20 w-20 mb-4 mt-4" src={image} alt={name + " Logo"} />
      <div class="bg-base-100 p-4 w-full h-max">
        <div class="text-xl font-bold">{name}</div>
        {#if price}
          <div class="text-lg">Price: {price}</div>
        {/if}
      </div>
      <button class="bg-accent text-base-100 py-2 w-full mt-auto">Buy Now</button>
    </div> -->

    <div class="card w-60 bg-base-100 shado w-xl">
        <figure class="bg-secondary py-5"><img src={image} alt={name+"Logo"}/></figure>
        <div class="card-body">
          <h2 class="card-title">Shoes!</h2>    
          <div class="text-lg">Price: {price}</div>
          <div class="card-actions justify-end">
            <button class="btn btn-primary" on:click={navigate}>Buy Now</button>
          </div>
        </div>
      </div>
  
  <style>

  </style>
  