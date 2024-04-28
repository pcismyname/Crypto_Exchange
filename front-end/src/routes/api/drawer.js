import { Writable } from "svelte-advanced-store";
import { uid } from "uid";
import { Contexts, Context } from "./Context";

class Section extends Writable {
    constructor(value, { component, props = {} } = {}, _parentThis) {
        super({ value, component, props });
        this._parentThis = _parentThis;
    }
}

class Sections extends Contexts {
    constructor({ label = "", value = "", expanded = true, ...options }) {
        options = {
            label,
            value,
            expanded,
            highlightedIndex: -1,
            selectedIndex: -1,
            items: [],
            ...options,
        };

        super(options);
    }

    item(value) {
        return this.findItem(value);
    }

    findItem(value) {
        return this.items.find((item) => item.value === value);
    }

    add(uid) {}

    addItem(value, component, props) {
        const section = new Section(value, component, props);
        this.items = [...this.items, section];
        return section;
    }

    addItems(items = []) {
        const _items = items.map(
            ({ value, ...item }) => new Section(item.value, { ...item }, this)
        );
        this.items = [...this.items, _items];
    }

    removeItem(value) {
        this.items = this.items.filter((item) => item.value !== value);
    }

    removeItems(values = []) {
        this.items = this.items.filter(
            (item) => values.indexOf(item.value) !== -1
        );
    }

    get highlightedItem() {
        return this.active.items[this.highlightedIndex];
    }

    highlightNext() {
        const items = this.suggestions;
        const currentIndex = this.highlightedIndex;

        if (currentIndex < items.length - 1) {
            this.highlightedIndex = currentIndex + 1;
        }
        return this.highlightedItem;
    }

    highlightPrev() {
        const currentIndex = this.highlightedIndex;

        if (currentIndex > -1) {
            this.highlightedIndex = currentIndex - 1;
        }
        return this.highlightedItem;
    }
}

class Drawer extends Contexts {
    constructor(options = {}) {
        options = {
            width: null,
            ...options,
        };
    }

    addDrawer(value, { isOpen, label }) {
        return this.addContext(value, { isOpen, label });
    }

    drawer(value) {
        return this.findContext(value);
    }
    removeDrawer(value) {
        return this.removeContext(value);
    }

    activateDrawer(value) {
        return this.activateContext(value);
    }
}
