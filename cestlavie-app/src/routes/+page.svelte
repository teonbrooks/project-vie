<script>
    import { siteTitle, siteDescription, siteImage, siteImageWidth, siteAuthor, siteURL, faviconImage } from '$lib/config';    
    import Tix from '$lib/components/Tix.svelte';
    
    export let names = ["a", "b", "c"];
    
</script>
    
<svelte:head>
    <title>{siteTitle}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta charset="utf-8" />
    <meta data-key="description" name="description" content="{siteDescription}">
    <meta name="author" content={siteAuthor}>
    <!-- Favicon -->
    <link rel="icon" type="image/svg" href={faviconImage} />
    <!-- Open Graph -->
    <meta property="og:type" content="profile" />
    <meta property="og:url" content={siteURL}>
    <meta property="og:title" content={siteTitle} />
    <meta property="og:description" content={siteDescription} />
    <meta property="og:image" content={siteImage} />
    <meta property="og:image:width" content={siteImageWidth} />
    <meta property="og:image:height" content={siteImageWidth} />
</svelte:head>

<p><em>pre-pre-pre-alpha</em></p>
<h1>Vie: <em>it's your life</em></h1>
<p>discovery and recommendations, curated by friends</p>
<p></p>

<div class='sample'>
    <!-- {#each names as title}
        <Tix {title}/>
    {/each} -->
    <img class="stub" src="data/labelling/images/stubs/b6fc8982-scrapbook_26-stub_06.jpg" alt="image of the Arc de Triomphe">
</div>

<style>
.sample {
    display: flex;
    flex-wrap: wrap;
    /* flex-flow: row wrap; */
    column-gap: 30px;
}

.stub {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
</style>