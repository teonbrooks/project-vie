<script>
	import { mdiClose } from '@mdi/js';
	import Card, { Content } from '@smui/card';
	import IconButton, { Icon } from '@smui/icon-button';
	import Dialog, { Content as DContent } from '@smui/dialog';
	import markdownit from 'markdown-it';
	import Stub from '$lib/components/Stub.svelte';

	export let path;
	export let item;
	export let width;
	export let height;
	const md = markdownit();
	let open = false;
</script>

<div>
	<div class="pushpin tilted">
		<div class="pinhead"></div>
		<div class="pinbase"></div>
		<div class="pinshaft"></div>
		<div class="pinpoint"></div>
	</div>
	<div class="stub card">
		<Card on:click={() => (open = true)}>
			<Content>
				{#if item.filename}
					<div class="image">
						<Stub {path} {item} {width} {height}/>
					</div>
				{/if}
			</Content>
		</Card>
	</div>
</div>
<Dialog bind:open sheet aria-describedby="sheet-content">
	<DContent id="sheet-content">
		<IconButton action="close" class="material-icons">
			<Icon tag="svg" viewBox="0 0 24 24">
				<path fill="currentColor" d={mdiClose} />
			</Icon>
		</IconButton>
		<div>
			{#if item.filename}
				<Stub {path} {item} width={""} height={""} />
			{/if}
			{#if item.description}
				<p>{@html md.render(item.description)}</p>
			{/if}
		</div>
	</DContent>
</Dialog>

<style>
	@import './css/pushpin.css';

	.image {
		display: grid;
		place-items: center;
	}

	.card:hover {
		cursor: pointer;
	}
</style>
