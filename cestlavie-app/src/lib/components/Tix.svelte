<!-- Notes for styling the ticket -->
<!-- https://freefrontend.com/css-tickets/ -->
<!-- https://medhatdawoud.net/blog/5-different-ways-to-create-a-ticket-layout -->
<script lang='ts'>
    // import Card, {Content} from '@smui/card';
    export let title = 'title';
    export let date = 'date';
    export let location = 'location';

    // let clicked = 0;

</script>

<div class="ticket-stub">
    <div>
        <h1>{title}</h1>
    </div>
    <div>
        <p>{date}</p>
        <p>{location}</p>
    </div>
</div>

<style>
    .ticket-stub {
        width: 60px;
        height: 100px;
        border: 1px solid black;
        border-radius: 5px;
        background-color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        }

        .ticket-stub h1 {
        font-size: 18px;
        font-weight: bold;
        }

        .ticket-stub p {
        font-size: 12px;
        }

</style>