<script>
    import Carousel from 'svelte-carousel';
    // ...
    export let images;
</script>

<Carousel
  let:loaded
>
  {#each images as src, imageIndex (src)}
    <div class="img-container">
      {#if loaded.includes(imageIndex)}
        <img loading="lazy" {src} alt="nature" />
      {/if}
    </div>
  {/each}
</Carousel>
