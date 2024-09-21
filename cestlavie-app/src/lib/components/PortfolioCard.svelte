<script>
	import { mdiLink, mdiClose } from '@mdi/js';
	import Card, { Content, Actions, ActionButtons, ActionIcons } from '@smui/card';
	import Button, { Label } from '@smui/button';
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

<Card>
	<Content>
		{#if item.filename}
			<div class="image">
				<Stub {path} {item} {width} {height}/>
			</div>
		{/if}
	</Content>
	<Actions style="align-items:end">
		<ActionButtons>
			<Button on:click={() => (open = true)}>
				<Label>Details</Label>
			</Button>
		</ActionButtons>
		<ActionIcons>
			<IconButton on:click={() => window.open(item.website)} title="Open Link">
				<Icon tag="svg" viewBox="0 0 24 24">
					<path fill="currentColor" d={mdiLink} />
				</Icon>
			</IconButton>
		</ActionIcons>
	</Actions>
</Card>
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
	.image {
		display: grid;
		place-items: center;
	}

</style>
