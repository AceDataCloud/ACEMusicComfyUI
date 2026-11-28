# ACE Music for ComfyUI

Clone this repository into ComfyUI/custom_nodes, install requirements.txt in the ComfyUI Python environment, set ACEDATACLOUD_API_TOKEN on the ComfyUI server and restart it.

```sh
python -m pip install -r requirements.txt
python -m unittest discover
```

Sign in to [Applications](https://platform.acedata.cloud/console/applications). On the **General Application** card, click the copy button beside **API KEY**. Confirm that the key has ACE Music access. If the application balance is low, click **Top Up** on its card. Set the raw key in the ComfyUI server environment as `ACEDATACLOUD_API_TOKEN` and restart ComfyUI. Keep keys out of prompts, shared workflows and commits.

| Action | Inputs or result |
| --- | --- |
| Create song from idea | Prompt and optional ACE Music model. |
| Create song from lyrics | Lyrics, style and title. |
| Import reference MP3 | Public HTTPS MP3 URL. Save the delivered track ID. |
| Cover a track | One owned track ID, lyrics and style. |
| Blend two tracks | Two distinct compatible owned track IDs, lyrics and style. |
| Generate lyrics | Prompt and optional style. Returns lyrics or a pending task ID. |
| Retrieve task / multiple tasks | Use the original task IDs. |
| List task history | Optional page and items per page. |

Audio creation, reference import and writing lyrics are separately priced. Use the creation tool once, save its `task_id`, then retrieve the same task. If the connection breaks before a task ID arrives, inspect task history before resubmitting. The task state and `response` carry completion and partial failures. A partial result can contain one usable track. Play delivered tracks from `response.data[].audio_url`. Read [ACE Music API documentation](https://github.com/AceDataCloud/ACEMusicAPI) and [current pricing](https://platform.acedata.cloud/services/024e09b4-52cf-5e98-a91a-efedf43104c4).
