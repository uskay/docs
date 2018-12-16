from shortcodes import Shortcode


class ComponentSamplerShortcode(Shortcode):
    name = 'component-sampler'
    template = 'views/partials/component-sampler.j2'
    strip = True
    render_empty = True

shortcode = ComponentSamplerShortcode
