// src/stores/cartStore.js
import { writable } from "svelte/store";

const initialState = {
    items: [],
    total: 0,
};

function createCart() {
    const { subscribe, set, update } = writable(initialState);

    return {
        subscribe,
        addItem: (product) => update(state => {
            const existingItem = state.items.find(item => item.id === product.id);

            if (existingItem) {
                // Update the existing item quantity and total price
                existingItem.quantity += product.quantity;
                state.total += product.price * product.quantity;
            } else {
                // Add a new item if it does not exist
                state.items.push({...product});
                state.total += product.price * product.quantity;
            }

            return state;
        }),
        removeItem: (productId) => update(state => {
            const index = state.items.findIndex(item => item.id === productId);

            if (index !== -1) {
                // Deduct the item's total contribution to the cart from the total and remove the item
                state.total -= state.items[index].price * state.items[index].quantity;
                state.items.splice(index, 1);
            }

            return state;
        }),
        clear: () => set(initialState),
    };
}

export const cart = createCart();

