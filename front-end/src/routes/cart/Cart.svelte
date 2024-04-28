<script>
    import { cart } from "../cartStore.js";
    import { goto } from "$app/navigation";

    async function navigate() {
        goto(`/cart/checkout`); // Pass coin data as context
    }
</script>

<div class="border rounded-lg overflow-hidden h-screen w-full">
    <table class="w-full">
        <thead class="bg-secondary">
            <tr>
                <th class="px-6 py-4 text-left font-medium">Product</th>
                <th class="px-6 py-4 text-left font-medium">Quantity</th>
                <th class="px-6 py-4 text-left font-medium">Price Per Coin</th>
                <th class="px-6 py-4 text-left font-medium">Remove</th>
            </tr>
        </thead>
        <tbody>
            {#each $cart.items as item (item.id)}
                <tr class="border-b dark:border-gray-700">
                    <td class="px-6 py-4 font-medium">{item.name}</td>
                    <td class="px-6 py-4">{item.quantity}</td>
                    <td class="px-6 py-4">${item.price.toFixed(2)}</td>
                    <td class="px-6 py-4">
                        <button
                            class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:text-accent-foreground h-10 w-10 text-red-500 hover:bg-red-100 dark:hover:bg-red-900"
                            on:click={() => cart.removeItem(item.id)}
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="24"
                                height="24"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                stroke-width="2"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                class="h-4 w-4"
                            >
                                <path d="M18 6 6 18" />
                                <path d="m6 6 12 12" />
                            </svg>
                            <span class="sr-only">Remove</span>
                        </button>
                    </td>
                </tr>
            {/each}
        </tbody>
    </table>
    <div class="flex justify-end mt-10">
        <div class="grid gap-2">
            <div class="flex items-center justify-between">
                <span class="font-medium">Total:</span>
                <span class="font-medium text-primary">{$cart.total}</span>
            </div>
            <div class="card-actions justify-end">
                <button class="btn btn-primary" on:click={navigate}
                    >Proceed to Checkout</button
                >
            </div>
        </div>
    </div>
</div>
