<!-- TradingViewWidget.svelte -->
<script>
    import { onMount } from 'svelte';
  
    onMount(() => {
      const script = document.createElement('script');
      script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js';
      script.async = true;
      script.innerHTML = JSON.stringify({
        "autosize": false, // Set autosize to false to control size
        "symbol": "CRYPTOCAP:BTC",
        "interval": "D",
        "timezone": "Etc/UTC",
        "theme": "dark",
        "style": "1",
        "locale": "en",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "calendar": false,
        "support_host": "https://www.tradingview.com",
        "width": "400",  // Set width
        "height": "300"  // Set height
      });
      
      document.getElementById('tradingview-widget').appendChild(script);
    });
  </script>
  
  <div class="tradingview-widget-container">
    <div
      id="tradingview-widget"
      class="tradingview-widget-container__widget"
    ></div>
  </div>
  