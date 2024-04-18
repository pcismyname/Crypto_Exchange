<!-- Detail.svelte -->
<script>
  import btc_img from "$lib/images/bitcoin.png";

  // Props for the component. Replace with actual dynamic values as needed.
  export let name = "BITCOIN";
  export let logo = btc_img; // Path to your logo image
  export let currentPrice = "$43,975.72";
  export let priceChange = "+2%";
  export let marketCap = "$826,445,951,378";
  export let marketCapChange = "+2%";
  export let fullyDiluted = "$915,435,574,336";
  export let fullyDilutedChange = "-2%";
</script>

<div class="card bg-secondary shadow-xl flex-row items-center p-4">
  <div class="flex flex-col items-center mr-4">
    <div class="badge badge-info gap-2">
      <img src={logo} alt={name} class="w-8 h-8" />
      <span>{name}</span>
    </div>
    <div class="mt-2 badge badge-outline flex-1"> descriptine will be here !!!!!!</div>
  </div>

  <div class="stats stats-vertical lg:stats-horizontal shadow">
    <div class="stat">
      <div class="stat-title">Current Price</div>
      <div class="stat-value text-info">{currentPrice}</div>
      <div class="stat-desc">{priceChange}</div>
    </div>

    <div class="stat">
      <div class="stat-title">Market Cap</div>
      <div class="stat-value">{marketCap}</div>
      <div class="stat-desc text-success">{marketCapChange}</div>
    </div>

    <div class="stat">
      <div class="stat-title">Fully Diluted</div>
      <div class="stat-value">{fullyDiluted}</div>
      <div class="stat-desc text-error">{fullyDilutedChange}</div>
    </div>
  </div>
</div>

<style>
  .badge-info {
    background: var(
      --tw-gradient-stops,
      var(--tw-color-opacity, 1) #3b82f6,
      var(--tw-color-opacity, 1) #9333ea,
      var(--tw-color-opacity, 1) #f43f5e
    );
    background-image: linear-gradient(90deg, var(--tw-gradient-stops));
  }
</style>
