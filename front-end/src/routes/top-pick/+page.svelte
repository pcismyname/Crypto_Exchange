<script>
  import bitcoin_img from "$lib/images/bitcoin.png";
  import etheruem_img from "$lib/images/etheruem.png";
  import usdt_img from "$lib/images/usdt.png";
  import xrp_img from "$lib/images/xrp.png";

  import Card from "../Card.svelte";

  //this shoud get data from server
  const coins = [
    {
      coinId: "btc",
      detail: { image: bitcoin_img, name: "Bitcoin", price: "$40,000" },
    },
    {
      coinId: "eth",
      detail: { image: etheruem_img, name: "etheruem", price: "$40,000" },
    },
    {
      coinId: "usdt",
      detail: { image: usdt_img, name: "Bitcoin", price: "$40,000" },
    },
    {
      coinId: "xrp",
      detail: { image: xrp_img, name: "Bitcoin", price: "$40,000" },
    },
  ];
</script>

<!-- <body class="flex flex-col h-dvh"> -->
  <div class="bg-primary pt-5 h-full">
    <p class="text-4xl mb-10 font-bold text-base-100 text-center">Top Pick</p>
    <div class="flex flex-wrap h-full bg-primary justify-center items-center gap-4">
      {#each coins as coin}
        <Card
          coinId={coin.coinId}
          image={coin.detail.image}
          name={coin.detail.name}
          price={coin.detail.price}
        />
      {/each}
      {#each coins as coin}
        <Card
          coinId={coin.coinId}
          image={coin.detail.image}
          name={coin.detail.name}
          price={coin.detail.price}
        />
      {/each}
    </div>
  </div>
<!-- </body> -->

