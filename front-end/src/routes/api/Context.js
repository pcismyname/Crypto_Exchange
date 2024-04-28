import { Writable } from "svelte-advanced-store";
import { noop } from "lodash";

class Context extends Writable {
    constructor(value, options = {}, _parentThis) {
        options = {
            value: value,
            trigger: noop,
            data: null,
            ...options,
        };
        super(options);
    }

    activate() {
        if (this._parentThis) {
            this._parentThis.activateContext(this.value);
        }
    }

    deactivate() {
        if (this._parentThis) {
            this._parentThis.deactivateContext(this.value);
        }
    }
}

class Contexts extends Writable {
    constructor(options) {
        options = {
            contexts: [],
            active: new Context("default", { data: {} }, this),
            ...options,
        };
        super(options);
        this.defaultContext = options.active;
    }

    addContext(
        value,
        { data, trigger, ...options } = {},
        ContextClass = Context
    ) {
        const context = new ContextClass(
            value,
            { data, trigger, ...options },
            this
        );
        this.contexts = [...this.contexts, context];
        return context;
    }

    context(value) {
        return this.findContext(value);
    }

    findContext(value) {
        return this.contexts.find((context) => context.value === value);
    }
    removeContext(value) {
        const targetContext = this.findContext(value);
        if (targetContext) {
            return this.contexts.filter((context) => context.value !== value);
        }
        return null;
    }

    activateContext(value) {
        const context = this.findContext(value);
        if (context) {
            this.active = context;
        } else {
            this.active = this.defaultContext;
        }
    }

    deactivateContext() {
        this.active = this.defaultContext;
    }

    get activeData() {
        return this.active.data;
    }

    set activeData(data) {
        this.active.data = data;
    }
}

export { Contexts, Context };
