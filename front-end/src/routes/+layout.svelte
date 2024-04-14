<script>
	import Header from './Header.svelte';
	import './styles.css';
	import '../app.css';
</script>

<div data-theme="mytheme">
	<Header />

	<main>
		<slot />
	</main>

	<footer>
		<p>created by <b> Chindsanuphong Pengchai </b></p>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		width: 100%;
		height: 100vh;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
