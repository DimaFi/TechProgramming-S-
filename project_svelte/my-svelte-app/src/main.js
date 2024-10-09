import App from './App.svelte';


const app = new App({
	target: document.body,
	props: {
		name: 'world'
	}
});

export const ssr = false;
export default app;

