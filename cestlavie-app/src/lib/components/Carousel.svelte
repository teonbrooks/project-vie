<script>
    import Carousel from 'svelte-carousel'
    // ...
    export let images;
</script>

<Carousel
  let:loaded
>
  {#each images as src}
    <div class="img-container">
      <img {src} alt="nature" />
    </div>
  {/each}
</Carousel>