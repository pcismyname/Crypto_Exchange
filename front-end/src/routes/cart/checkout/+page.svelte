<script>
    import { cart } from "../../cartStore.js";
    import { goto } from "$app/navigation";
    console.log($cart.items);
    let isModalOpen = false;
    async function pay() {
        isModalOpen = true;
    }

    async function confirm() {
        isModalOpen = false;
        const baseUrl = "http://localhost:8002/api/v1/inventory";

        // Ensure fetchPromises are correctly formed
        const fetchPromises = $cart.items.map((item) => {
            const url = `${baseUrl}/${item.id}/decrease?amount=${item.quantity}`;
            return fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                    // Include authorization or other necessary headers
                },
                body: JSON.stringify({
                    crypto_id: item.id,
                    amount: item.quantity,
                }),
            });
        });

        try {
            const responses = await Promise.all(fetchPromises);
            // Process responses
            responses.forEach(async (response) => {
                if (!response.ok) {
                    console.error(
                        `Failed to decrease inventory for item with response status: ${response.status}`
                    );
                } else {
                    const data = await response.json();
                    console.log("Decrease Inventory Response:", data);
                    console.log("Cart store:", cart);
                    console.log("Clear method:", cart.clear);
                    cart.clear();
                    goto(`/top-pick`)
                }
            });
        } catch (error) {
            console.error("Error in decreasing inventory:", error);
        }
    }
</script>

<div class="container mx-auto max-w-4xl py-12 px-4 md:px-6">
    <div class="grid grid-cols-1 gap-8 md:grid-cols-2">
        <div class="space-y-6">
            <div>
                <h2 class="text-2xl font-bold">Billing Address</h2>
                <p class="text-gray-500 dark:text-gray-400">
                    Enter your billing address details.
                </p>
            </div>
            <div class="space-y-4">
                <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
                    <div class="space-y-2">
                        <label
                            class=" text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                            for="name"
                        >
                            Name
                        </label>
                        <input
                            class=" flex h-10 w-full rounded-md border border-input px-3 py-2 text-sm"
                            id="name"
                            placeholder="John Doe"
                        />
                    </div>
                    <div class="space-y-2">
                        <label
                            class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                            for="address1"
                        >
                            Address Line 1
                        </label>
                        <input
                            class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                            id="address1"
                            placeholder="123 Main St"
                        />
                    </div>
                </div>
                <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
                    <div class="space-y-2">
                        <label
                            class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                            for="address2"
                        >
                            Address Line 2
                        </label>
                        <input
                            class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                            id="address2"
                            placeholder="Apt 123"
                        />
                    </div>
                    <div class="space-y-2">
                        <label
                            class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                            for="city"
                        >
                            City
                        </label>
                        <input
                            class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                            id="city"
                            placeholder="New York"
                        />
                    </div>
                </div>
                <div class="grid grid-cols-1 gap-4 sm:grid-cols-3">
                    <div class="space-y-2">
                        <label
                            class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                            for="state"
                        >
                            State
                        </label>
                        <input
                            class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                            id="state"
                            placeholder="NY"
                        />
                    </div>
                    <div class="space-y-2">
                        <label
                            class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                            for="zip"
                        >
                            Zip Code
                        </label>
                        <input
                            class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                            id="zip"
                            placeholder="10001"
                        />
                    </div>
                    <div class="space-y-2">
                        <label
                            class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                            for="country"
                        >
                            Country
                        </label>
                        <button
                            type="button"
                            role="combobox"
                            aria-controls="radix-:r22:"
                            aria-expanded="false"
                            aria-autocomplete="none"
                            dir="ltr"
                            data-state="closed"
                            data-placeholder=""
                            class="flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                        >
                            <span style="pointer-events: none;"
                                >Select a country</span
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
                                class="h-4 w-4 opacity-50"
                                aria-hidden="true"
                            >
                                <path d="m6 9 6 6 6-6"></path>
                            </svg>
                        </button>
                        <select
                            aria-hidden="true"
                            tabindex="-1"
                            style="position: absolute; border: 0px; width: 1px; height: 1px; padding: 0px; margin: -1px; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); white-space: nowrap; overflow-wrap: normal;"
                        >
                            <option value=""></option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
        <div class="space-y-6">
            <div>
                <h2 class="text-2xl font-bold">Wallet Address</h2>
                <p class="text-gray-500 dark:text-gray-400">
                    Enter your cryptocurrency wallet address.
                </p>
            </div>
            <div class="space-y-2">
                <label
                    class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                    for="wallet"
                >
                    Wallet Address
                </label>
                <input
                    class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                    id="wallet"
                    placeholder="0x123456789abcdef0123456789abcdef01234567"
                />
            </div>
        </div>
    </div>
    <div class="flex justify-end">
        <div class="grid gap-2">
            <div class="flex items-center justify-between">
                <span class="font-extrabold text-lg">Total: $</span>
                <span class="font-extrabold text-lg">{$cart.total}</span>
            </div>
        </div>
    </div>

    <div class="mt-8 flex justify-end">
        <div class="card-actions justify-end">
            <button class="btn btn-primary" on:click={pay}>Pay Now</button>
        </div>
    </div>
</div>

<div class="modal justify-center" class:modal-open={isModalOpen}>
    <div class="modal-box">
        <h3 class="font-bold text-lg justify-center">scan PromptPay</h3>
        <img src="https://promptpay.io/0650474865.png" alt="qr-code" />
        <div class="modal-action">
            <!-- 🔵 set false on click -->
            <button class="btn" on:click={confirm}>Ok!</button>
        </div>
    </div>
</div>
