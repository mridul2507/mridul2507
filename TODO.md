# TODO - Complete Repository Cleanup

## Step 1: Fix merge conflicts in data/contributions.json
- [x] Resolve `<<<<<<< HEAD / ======= / >>>>>>>` conflict
- [x] Run `convert_data.py` to regenerate from fresh contrib.json data

## Step 2: Fix merge conflicts in contrib-heatmap.svg
- [x] Resolve merge conflict (keep render_heatmap_svg.py version)
- [x] Run `render_heatmap_svg.py` to regenerate

## Step 3: Rename avi-ascii.svg → mridul-ascii.svg
- [x] Create `mridul-ascii.svg` with same content
- [x] Delete `avi-ascii.svg`

## Step 4: Update README.md
- [x] Replace alt text "Avi Vashishta" → "Mridul Srivastava"
- [x] Replace alt text "AVI" → "MS"
- [x] Update image source `avi-ascii.svg` → `mridul-ascii.svg`

## Step 5: Update make_ascii_svg.py
- [x] Change default output from `avi-ascii.svg` → `mridul-ascii.svg`

## Step 6: Update docs/3d-ascii-wordmark.md
- [x] Replace all "AVI" references with "MS"
- [x] Remove/fix blog link to avivashishta.com

## Step 7: Final verification
- [x] Run all scripts to regenerate files
- [x] Verify no "avi" references remain

