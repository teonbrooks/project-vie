<script>
    import Tix from '$lib/components/Tix.svelte';
    export let names = ["a", "b", "c"];
</script>


<h1>Vie: <em>it's your life</em></h1>
<p>discovery and recommendations, curated by friends</p>
<p></p>

<div class='sample'>
    {#each names as title}
        <Tix {title}/>
    {/each}
</div>

<style>
.sample {
    display: flex;
    flex-wrap: wrap;
    /* flex-flow: row wrap; */
    column-gap: 30px;
}
</style>