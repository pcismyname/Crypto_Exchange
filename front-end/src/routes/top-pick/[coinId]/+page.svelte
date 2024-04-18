<!-- TradingViewWidget.svelte -->
<script>
  import { onMount } from "svelte";
  import Detail from '../Detail.svelte'
  import Buy from '../Buy.svelte'

  /** @type {import('./$types').PageData} */
  export let data;
  console.log(data);

  onMount(() => {
    const script = document.createElement("script");
    script.src =
      "https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js";
    script.async = true;
    script.innerHTML = JSON.stringify({
      autosize: false, // Set autosize to false to control size
      symbol: "CRYPTOCAP:BTC",
      interval: "D",
      timezone: "Etc/UTC",
      theme: "dark",
      style: "1",
      locale: "en",
      enable_publishing: false,
      allow_symbol_change: true,
      calendar: false,
      support_host: "https://www.tradingview.com",
      width: "950", // Set width
      height: "500", // Set height
    });

    document.getElementById("tradingview-widget").appendChild(script);
  });
</script>

<body class="flex flex-col">
  <div class="bg-primary h-screen">
    <!-- <h1>{data.coinDetails.name}</h1>
    <p>Price: {data.coinDetails.price}</p>
    <p>{data.coinDetails.description}</p> -->

    <!-- <Detail/>
    <Buy/>

    <div class="tradingview-widget-container">
      <div
        id="tradingview-widget"
        class="tradingview-widget-container__widget"
      ></div>
    </div>
  </div> -->

  <div class="container mx-auto px-4 py-8">
    <!-- First row for Detail component -->
    <div class="mb-8">
      <Detail {...data} />
    </div>
  
    <!-- Second row for TradingView widget and Buy component -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <!-- TradingView widget container -->
      <div class="md:col-span-2">
        <div id="tradingview-widget" class="tradingview-widget-container__widget"></div>
      </div>
  
      <!-- Buy component container -->
      <div class="md:col-span-1">
        <Buy coinName={data.name} coinSymbol="BTC" />
      </div>
    </div>
  </div>
  
</body>
