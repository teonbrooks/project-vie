<script>
	import Carousel from "$lib/components/Carousel.svelte";
	
	export let data;

	// consider using the route as the property name for the collection
	const images = data.pages;

</script>

<svelte:head>
	<title>Carousel</title>
</svelte:head>

<h1>Scrapbook</h1>   

<!-- <Carousel {images} /> -->
