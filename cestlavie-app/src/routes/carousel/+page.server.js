export const prerender = true

export const load = async ({ url, fetch }) => {
    const Res = await fetch(`${url.origin}/api/scrapbook/stub_text_extraction.toml`)
    const collection = await Res.json()

    var pages = Object.keys(import.meta.glob('/static/data/labelling/images/*.jpg'));
    pages = pages.map(page => page.slice(8))
    
    const path = '/data/labelling/images/stubs'

    return { collection, path, pages }
}
