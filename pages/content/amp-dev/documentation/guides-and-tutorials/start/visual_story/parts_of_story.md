---
$title: Understanding the parts of an AMP story
$order: 2
---

An AMP story is a full-screen visual storytelling experience that conveys information with images, videos, graphics, audio, and more. It's perfect for users who want bite-sized, visually-rich content.  

The basic ingredients that go into an AMP story are individual **pages**. These pages, in turn, are composed of individual **layers** that contain basic HTML and AMP **elements**.

{{ image('/static/img/docs/tutorials/amp_story/story_parts.png', 1047, 452, align='center ninety') }}

Each of those ingredients are translated into AMP components, where the story is represented by `amp-story`, the page is represented by `amp-story-page`, and the layers are represented by `amp-story-grid-layer`.

{{ image('/static/img/docs/amp-story-tag-hierarchy.png', 557, 355, align='center seventyfive' ) }}

Let's start creating our story with the `amp-story` container.

<div class="prev-next-buttons">
  <a class="button prev-button" href="{{g.doc('/content/amp-dev/documentation/guides-and-tutorials/start/visual_story/setting_up.md', locale=doc.locale).url.path}}"><span class="arrow-prev">Prev</span></a>
  <a class="button next-button" href="{{g.doc('/content/amp-dev/documentation/guides-and-tutorials/start/visual_story/start_story.md', locale=doc.locale).url.path}}"><span class="arrow-next">Next</span></a>
</div>
