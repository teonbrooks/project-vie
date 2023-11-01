<script>
    import Tix from '$lib/components/Tix.svelte';
    export let names = ["a", "b", "c"];
</script>


<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

{#each names as title}
    <Tix {title}/>
{/each}
