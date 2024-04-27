<!-- Detail.svelte -->
<script>
    import bitcoin_img from "$lib/images/bitcoin.png";
    import etheruem_img from "$lib/images/etheruem.png";
    import usdt_img from "$lib/images/usdt.png";
    import xrp_img from "$lib/images/xrp.png";
    // Props for the component. Replace with actual dynamic values as needed.
    export let name = "";
    export let logo = ""; // Path to your logo image
    export let usd = "";
    export let marketCap = "";
    export let usd_24h_vol = "";
    const images = {
        btc: bitcoin_img,
        eth: etheruem_img,
        usdt: usdt_img,
        xrp: xrp_img,
    };
</script>

<div class="card bg-secondary shadow-xl flex-row items-center p-4">
    <div class="flex flex-col items-center mr-4">
        <div class="badge badge-info gap-2">
            <img src={images[logo.toLowerCase()]} alt={name} class="w-8 h-8" />
            <span>{name.toUpperCase()}</span>
        </div>
    </div>

    <div class="stats stats-vertical lg:stats-horizontal shadow">
        <div class="stat">
            <div class="stat-title">usd</div>
            <div class="stat-value text-info">${usd}</div>
        </div>

        <div class="stat">
            <div class="stat-title">marketCap</div>
            <div class="stat-value">${marketCap}</div>
        </div>

        <div class="stat">
            <div class="stat-title">usd_24h_vol</div>
            <div class="stat-value">${usd_24h_vol}</div>
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
