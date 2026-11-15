from pathlib import Path

import cv2


VISION_DIR = Path(__file__).parent
SCREENSHOT_DIR = VISION_DIR / "screenshots"
CROP_DIR = VISION_DIR / "card_crops"

DISPLAY_SCALE = 0.3

SCREENSHOTS = [
    "hand01_preflop_full.png",
    "hand01_flop_full.png",
    "hand01_turn_full.png",
    "hand01_river_full.png"
]


def convert_to_original_size(region):
    x, y, width, height = region

    return (
        round(x / DISPLAY_SCALE),
        round(y / DISPLAY_SCALE),
        round(width / DISPLAY_SCALE),
        round(height / DISPLAY_SCALE)
    )


def crop_region(image, region):
    x, y, width, height = region
    return image[y:y + height, x:x + width]


def main():
    reference_path = SCREENSHOT_DIR / "hand01_river_full.png"
    reference_image = cv2.imread(str(reference_path))

    if reference_image is None:
        raise FileNotFoundError(f"Could not open {reference_path}")

    # Resize only the displayed image, not the saved screenshots
    display_image = cv2.resize(
        reference_image,
        None,
        fx=DISPLAY_SCALE,
        fy=DISPLAY_SCALE
    )

    print("Draw a box around your two cards, then press Enter.")

    displayed_player_region = cv2.selectROI(
        "Select Player Cards",
        display_image,
        showCrosshair=True
    )

    cv2.destroyWindow("Select Player Cards")

    print("Draw a box around the top-right community cards, then press Enter.")

    displayed_community_region = cv2.selectROI(
        "Select Community Cards",
        display_image,
        showCrosshair=True
    )

    cv2.destroyAllWindows()

    player_region = convert_to_original_size(displayed_player_region)
    community_region = convert_to_original_size(displayed_community_region)

    CROP_DIR.mkdir(exist_ok=True)

    for filename in SCREENSHOTS:
        image = cv2.imread(str(SCREENSHOT_DIR / filename))

        if image is None:
            print(f"Could not open {filename}")
            continue

        player_crop = crop_region(image, player_region)
        community_crop = crop_region(image, community_region)

        stage = filename.replace("_full.png", "")

        cv2.imwrite(
            str(CROP_DIR / f"{stage}_player.png"),
            player_crop
        )

        cv2.imwrite(
            str(CROP_DIR / f"{stage}_community.png"),
            community_crop
        )

        print(f"Cropped {filename}")

    print("Finished. Check vision/card_crops/")


if __name__ == "__main__":
    main()