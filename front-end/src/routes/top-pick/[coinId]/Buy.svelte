<script>
    import { cart } from "../../cartStore.js"; // Assuming cart store is in a separate file
    import { goto } from "$app/navigation";

    export let name = "";
    export let crypto_id = "";
    export let symbol = "";
    export let price = "";
    let quantity = 0.0000000001; // Default minimum quantity
    let totalCost = price * quantity; // Calculate initial total cost

    function handleQuantityInput(event) {
        const newQuantity = parseFloat(event.target.value);
        if (!isNaN(newQuantity) && newQuantity >= 0.0000000001) {
            quantity = newQuantity;
            totalCost = price * quantity; // Update total cost whenever quantity changes
        }
    }

    function handleTotalCostInput(event) {
        const newTotalCost = parseFloat(event.target.value);
        if (!isNaN(newTotalCost) && newTotalCost > 0) {
            totalCost = newTotalCost;
            quantity = totalCost / price; // Update quantity whenever total cost changes
        }
    }

    function addToCart() {
      console.log(crypto_id, name, symbol, price, quantity)
        if (price && quantity) {
            cart.addItem({
                id: crypto_id, 
                name: name,
                symbol: symbol,
                price: parseFloat(price),
                quantity: parseFloat(quantity),
            });
        }
        goto(`/cart`);
    }
    console.log(cart)
</script>

<div class="card w-144 h-3/4 bg-secondary">
    <div class="card-body items-center text-center">
        <h2 class="card-title">{name.toUpperCase()}</h2>
        <div class="flex flex-col">
            <div class="form-control">
                <label class="input-group input-group-vertical input-group-lg">
                    <span>Price ($)</span>
                    <input
                        type="number"
                        min="0.0000000001"
                        placeholder="Price"
                        class="input input-bordered"
                        bind:value={totalCost}
                        on:input={handleTotalCostInput}
                    />
                </label>
            </div>
            <div class="form-control mt-4">
                <label class="input-group input-group-vertical input-group-lg">
                    <span>Quantity</span>
                    <input
                        type="number"
                        min="0.0000000001"
                        placeholder="Quantity"
                        class="input input-bordered"
                        bind:value={quantity}
                        on:input={handleQuantityInput}
                    />
                </label>
            </div>
        </div>
        <div class="card-actions mt-6">
            <button class="btn btn-primary btn-wide" on:click={addToCart}
                >Buy {symbol}</button
            >
        </div>
    </div>
</div>
