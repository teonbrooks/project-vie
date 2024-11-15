export const prerender = true

export const load = async ({ url, fetch }) => {

    var pages = Object.keys(import.meta.glob('/static/images/full_res/*.jpg'));
    pages = pages.map(page => page.slice(8))

    return { pages }
}
