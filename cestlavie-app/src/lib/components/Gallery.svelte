<script>
	import LayoutGrid, { Cell } from '@smui/layout-grid';
	import PortfolioCard from './PortfolioCard.svelte';

	export let items = [];
	export let path;

</script>

<article id="portfolio" class="panel">
	<!-- <LayoutGrid> -->
	<div id="wrapper">
		{#each items.slice(0, 12) as item}
			<div class="cell">
				<div>
					<div class="pushpin tilted">
						<div class="pinhead"></div>
						<div class="pinbase"></div>
						<div class="pinshaft"></div>
						<div class="pinpoint"></div>
					</div>
				</div>
				<Cell>
					<PortfolioCard {path} {item} width={"250px"} height={""}/>
				</Cell>
			</div>
		{/each}
	</div>
	<!-- </LayoutGrid> -->
</article>

<style>
	.cell {
	  display: flex;
	  justify-content: center;
	  align-items: center;
	  color: var(--mdc-theme-on-secondary, #fff);
	}

	#wrapper {
		display: grid;
		grid-template-columns: repeat(4, 2fr);
		}
	
	@import './css/pushpin.css'

  </style>