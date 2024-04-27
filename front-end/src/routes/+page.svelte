<script>
  import main_img from "$lib/images/main_img.png";
</script>

<svelte:head>
  <title>BITX</title>
</svelte:head>

<body class="flex flex-col">
  <!-- Main content container -->
  <div class="bg-primary flex-1 flex items-center justify-center space-x-48">
    <div class="space-y-10 	mx-0 flex flex-col items-center">
      <h1 class="text-6xl font-bold text-secondary">
        Buy Crypto<br />
        Just one Click
      </h1>
      <p class="text-xl text-base-100 text-center">
        Join the most trusted crypto platform in the world<br />
        No extra fee<br/>
        Buy anywhere and anytime.
      </p>
      <a class="btn btn-accent text-base-100 w-80" href="/top-pick">Buy  Now</a>
    </div>

    <div>
      <img src={main_img} alt="Buy Crypto" class="w-full max-w-md mx-auto" />
    </div>
  </div>
</body>

