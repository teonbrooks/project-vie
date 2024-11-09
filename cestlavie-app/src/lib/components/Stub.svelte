<script>
    export let path;
    export let item = {'filename': ''};
    export let width;
    export let height;

</script>
<img loading="lazy" src="{path}/{item.filename}"
     alt='ticket stub for {item.filename}'
        width={width}
        height={height}
	 />