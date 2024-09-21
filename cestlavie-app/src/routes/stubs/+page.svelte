<script>
	import Carousel from "$lib/components/Carousel.svelte";
	import Gallery from "$lib/components/Gallery.svelte";
	
	export let data;

	// consider using the route as the property name for the collection
	const items = data.collection.stubs;
	const path = data.path;
	const images = data.pages;

</script>

<svelte:head>
	<title>Ticket Stubs Gallery</title>
</svelte:head>

<h1>Ticket Stubs</h1>   

<div id='frame'>
	<!-- <Carousel {images} /> -->
	<Gallery {path} {items} />
</div>

<style>
	div#frame {
    background: url(images/corkboard.jpg) no-repeat center fixed;
    background-position: right 100px;
	background-size: 100% 100%;
	}

	h1 {
  	height: 3rem;
  	position: sticky;
  	top: 0;
	}

</style>