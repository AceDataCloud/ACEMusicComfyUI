from . import nodes

NODE_CLASS_MAPPINGS = {
    "AceMusicGenerate": nodes.AceMusicGenerate,
    "AceMusicCustom": nodes.AceMusicCustom,
    "AceMusicUpload": nodes.AceMusicUpload,
    "AceMusicCover": nodes.AceMusicCover,
    "AceMusicMashup": nodes.AceMusicMashup,
    "AceMusicLyrics": nodes.AceMusicLyrics,
    "AceMusicRetrieve": nodes.AceMusicRetrieve,
    "AceMusicBatch": nodes.AceMusicBatch,
    "AceMusicHistory": nodes.AceMusicHistory,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AceMusicGenerate": "ACE Music · Create song from idea",
    "AceMusicCustom": "ACE Music · Create song from lyrics",
    "AceMusicUpload": "ACE Music · Import reference MP3",
    "AceMusicCover": "ACE Music · Cover a track",
    "AceMusicMashup": "ACE Music · Blend two tracks",
    "AceMusicLyrics": "ACE Music · Generate lyrics",
    "AceMusicRetrieve": "ACE Music · Retrieve task",
    "AceMusicBatch": "ACE Music · Retrieve multiple tasks",
    "AceMusicHistory": "ACE Music · List task history",
}
