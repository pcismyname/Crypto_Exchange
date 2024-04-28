// src/stores/cartStore.js
import { writable } from "svelte/store";

const initialState = {
    items: [ { id: 1, name: 'Product 1', price: 19.99 },
    { id: 2, name: 'Product 2', price: 29.99 },
    { id: 3, name: 'Product 3', price: 39.99 },],
    total: 0,
};

function  createCart() {
    const { subscribe, set, update } = writable(initialState);

    return {
        subscribe,
        addItem: (product) =>
            update((state) => {
                const index = state.items.findIndex(
                    (item) => item.id === product.id
                );

                if (index !== -1) {
                    state.items[index].quantity += 1;
                } else {
                    state.items.push({ ...product, quantity: 1 });
                }

                state.total += product.price;
                return state;
            }),
        removeItem: (productId) =>
            update((state) => {
                const index = state.items.findIndex(
                    (item) => item.id === productId
                );

                if (index !== -1) {
                    state.total -=
                        state.items[index].price * state.items[index].quantity;
                    state.items.splice(index, 1);
                }

                return state;
            }),
        clear: () => set(initialState),
    };
}

export let cart = createCart();
