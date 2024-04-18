<script>
    import btc_img from "$lib/images/bitcoin.png";
    export let coinName = "Bitcoin";
    export let coinSymbol = "BTC";
    export let logo = btc_img;
  </script>
  
  <div class="card w-96 bg-base-100 shadow-xl image-full">
    <img src={logo} class="w-8 h-8" />
    <div class="card-body items-center text-center">
      <h2 class="card-title">{coinName}</h2>
      <div class="form-control">
        <label class="input-group input-group-vertical input-group-lg">
          <span>Price</span>
          <input type="number" placeholder="Price" class="input input-bordered" />
        </label>
      </div>
      <div class="form-control mt-4">
        <label class="input-group input-group-vertical input-group-lg">
          <span>Quantity</span>
          <input type="number" placeholder="Quantity" class="input input-bordered" />
        </label>
      </div>
      <div class="card-actions mt-6">
        <button class="btn btn-primary btn-wide">Buy {coinSymbol}</button>
      </div>
    </div>
  </div>
  
  <style>
    .image-full figure {
      height: 100px; /* Adjust as per your image's aspect ratio */
      background-color: var(--tw-gradient-stops);
      background-image: linear-gradient(135deg, #6b73ff, #000dff);
    }
  </style>
  