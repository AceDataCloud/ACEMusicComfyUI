"""ComfyUI nodes for ACE Music. The server owns the credential."""

import json
import os

from .client import invoke


class AceMusicNode:
    CATEGORY = "Ace Data Cloud/ACE Music"
    FUNCTION = "run"
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("task_id", "result_json")
    OUTPUT_NODE = True

    def run(self, **values):
        result = invoke(
            os.environ.get("ACEDATACLOUD_API_TOKEN"), self.operation, values
        )
        text = json.dumps(result, ensure_ascii=False)
        task_id = result.get("task_id") or result.get("id") or ""
        return {"result": (task_id, text), "ui": {"text": [text]}}


class TaskReadNode(AceMusicNode):
    @classmethod
    def IS_CHANGED(cls, **values):
        # An existing task or history page can change between graph executions.
        return float("nan")


class AceMusicGenerate(AceMusicNode):
    operation = "generate"
    DESCRIPTION = "Submit one paid song generation. Save its task ID."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"prompt": ("STRING", {"multiline": True, "default": ""})},
            "optional": {"model": (["acemusic-v1.1", "acemusic-v1"], {})},
        }


class AceMusicCustom(AceMusicNode):
    operation = "custom"
    DESCRIPTION = (
        "Submit one paid song generation with your own lyrics, style and title."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lyric": ("STRING", {"multiline": True, "default": ""}),
                "style": ("STRING", {"multiline": True, "default": ""}),
                "title": ("STRING", {"multiline": False, "default": ""}),
            },
            "optional": {"model": (["acemusic-v1.1", "acemusic-v1"], {})},
        }


class AceMusicUpload(AceMusicNode):
    operation = "upload"
    DESCRIPTION = (
        "Import one publicly accessible HTTPS MP3 as a separately priced reference."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"audio_url": ("STRING", {"multiline": False, "default": ""})},
            "optional": {
                "name": ("STRING", {"multiline": False, "default": ""}),
                "audio_id": ("STRING", {"multiline": False, "default": ""}),
            },
        }


class AceMusicCover(AceMusicNode):
    operation = "cover"
    DESCRIPTION = (
        "Submit one paid cover using a caller-owned track ID and new lyrics and style."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio_id": ("STRING", {"multiline": False, "default": ""}),
                "lyric": ("STRING", {"multiline": True, "default": ""}),
                "style": ("STRING", {"multiline": True, "default": ""}),
            },
            "optional": {
                "title": ("STRING", {"multiline": False, "default": ""}),
                "audio_influence": ("FLOAT", {"default": 60, "min": 1, "max": 100}),
            },
        }


class AceMusicMashup(AceMusicNode):
    operation = "mashup"
    DESCRIPTION = (
        "Submit one paid mashup with two distinct, compatible caller-owned track IDs."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first_audio_id": ("STRING", {"multiline": False, "default": ""}),
                "second_audio_id": ("STRING", {"multiline": False, "default": ""}),
                "lyric": ("STRING", {"multiline": True, "default": ""}),
                "style": ("STRING", {"multiline": True, "default": ""}),
            },
            "optional": {
                "title": ("STRING", {"multiline": False, "default": ""}),
                "audio_influence": ("FLOAT", {"default": 60, "min": 1, "max": 100}),
            },
        }


class AceMusicLyrics(AceMusicNode):
    operation = "lyrics"
    DESCRIPTION = "Request paid lyrics independently. The reply may contain lyrics or a pending task ID."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"prompt": ("STRING", {"multiline": True, "default": ""})},
            "optional": {"style": ("STRING", {"multiline": True, "default": ""})},
        }


class AceMusicRetrieve(TaskReadNode):
    operation = "retrieve"
    DESCRIPTION = (
        "Read the same task ID. Inspect its state and response for tracks or lyrics."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"task_id": ("STRING", {"multiline": False, "default": ""})},
            "optional": {},
        }


class AceMusicBatch(TaskReadNode):
    operation = "batch"
    DESCRIPTION = "Read 1 to 100 existing task IDs, one per line."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"task_ids": ("STRING", {"multiline": True, "default": ""})},
            "optional": {},
        }


class AceMusicHistory(TaskReadNode):
    operation = "history"
    DESCRIPTION = "Read one page of the authenticated application’s task history."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "page": ("INT", {"default": 1, "min": 1, "max": 10001}),
                "page_size": ("INT", {"default": 20, "min": 1, "max": 100}),
            },
        }
