# See https://tech.davis-hansson.com/p/make/
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

original_images=$(wildcard cestlavie-app/static/images/originals/*.jpg cestlavie-app/static/images/originals/**/*.jpg)
stripped_images=$(subst originals,exif_stripped, $(original_images))
thumb_images=$(subst originals,thumbs, $(original_images))
full_images=$(subst originals,full, $(original_images))
thumb_webp_images=$(subst jpg,webp, $(thumb_images))
full_webp_images=$(subst jpg,webp, $(full_images))

cestlavie-app/static/images/exif_stripped/%.jpg: cestlavie-app/static/images/originals/%.jpg
> mkdir -p cestlavie-app/static/images/exif_stripped/stubs
> exiftool -all= -o $@ $<

## Scale and optimize all the images.
optimize-images: $(thumb_images) $(full_images) $(thumb_webp_images) $(full_webp_images)
.PHONY: optimize-images

cestlavie-app/static/images/thumbs/%.jpg: cestlavie-app/static/images/exif_stripped/%.jpg
> mkdir -p cestlavie-app/static/images/thumbs/stubs
> convert $< -resize 633x474 -strip $@
> jpegoptim -sq $@

cestlavie-app/static/images/full/%.jpg: cestlavie-app/static/images/exif_stripped/%.jpg
> mkdir -p cestlavie-app/static/images/full/stubs
# > convert $< -resize 1688x1264 -strip $@
> convert $< -strip $@
> jpegoptim -sq $@

cestlavie-app/static/images/thumbs/%.webp: cestlavie-app/static/images/exif_stripped/%.jpg
> mkdir -p cestlavie-app/static/images/full/stubs
> cwebp $< -q 75 -z 6 -resize 633 0 -o $@

cestlavie-app/static/images/full/%.webp: cestlavie-app/static/images/exif_stripped/%.jpg
> mkdir -p cestlavie-app/static/images/full/stubs
> cwebp $< -q 75 -z 6 -o $@

cestlavie-app/static/images/exif_stripped/stubs/%.jpg: cestlavie-app/static/images/originals/stubs/%.jpg
> mkdir -p cestlavie-app/static/images/exif_stripped/stubs
> exiftool -all= -o $@ $<

cestlavie-app/static/images/thumbs/stubs/%.jpg: cestlavie-app/static/images/exif_stripped/stubs/%.jpg
> mkdir -p cestlavie-app/static/images/thumbs/stubs
> convert $< -resize 633x474 -strip $@

cestlavie-app/static/images/full/stubs/%.jpg: cestlavie-app/static/images/exif_stripped/stubs/%.jpg
> mkdir -p cestlavie-app/static/images/full/stubs
> convert $< -strip $@

cestlavie-app/static/images/thumbs/stubs/%.webp: cestlavie-app/static/images/exif_stripped/stubs/%.jpg
> mkdir -p cestlavie-app/static/images/full/stubs
> cwebp $< -q 75 -z 6 -resize 633 0 -o $@

cestlavie-app/static/images/full/stubs/%.webp: cestlavie-app/static/images/exif_stripped/stubs/%.jpg
> mkdir -p cestlavie-app/static/images/full/stubs
> cwebp $< -q 75 -z 6 -o $@
