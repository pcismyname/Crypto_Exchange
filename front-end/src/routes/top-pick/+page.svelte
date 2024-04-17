<script>
  import bitcoin_img from "$lib/images/bitcoin.png";
  import etheruem_img from "$lib/images/etheruem.png";
  import usdt_img from "$lib/images/usdt.png";
  import xrp_img from "$lib/images/xrp.png";

  import Card from "../Card.svelte";
</script>

<body class="flex flex-col">
<div class="bg-primary pt-5  h-screen">
  <p class="text-4xl mb-10 font-bold text-base-100 text-center">
    Top Pick
  </p>
  <div class="flex flex-wrap justify-center items-center gap-4">
    <Card image={bitcoin_img} name="Bitcoin" price="$40,000" targetUrl="main-coin"/>
    <Card image={etheruem_img} name="Etheruem" price="$10,000" />
    <Card image={usdt_img} name="USDT" price="$1" />
    <Card image={xrp_img} name="XRP" price="$10" />
  </div>
</div>
</body>
<style lang="postcss"></style>
