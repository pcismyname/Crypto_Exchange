<script>
    import Header from "./Header.svelte";
    import "./styles.css";
    import "../app.css";
    import Transition from './Transition.svelte';

    /** @type {import('./$types').PageData} */
    export let data;
</script>

<div data-theme="mytheme">
	<Transition key={data.url} duration={600}/>
    <Header />

    <main>
        <slot />
    </main>

    <footer>
        <p>created by <b> Chindsanuphong Pengchai </b></p>
    </footer>
</div>

<style>
    main {
        width: 100%;
        /* height: 100vh; */
        min-height: calc(100vh - var(--global-footer-height));
    }
    footer {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 12px;
        height: var(--global-footer-height);
    }

    @media (min-width: 480px) {
        footer {
            padding: 12px 0;
        }
    }
</style>
