{
    'targets': [{
        'defines': ['NAPI_VERSION=2'],
        'target_name': 'ffmpeg',
        'sources': [
            'native/src/ffmpeg.c',
        ],
        'conditions': [
            ['OS=="linux"', {
                'sources': [
                    'native/src/linux-ffmpeg.c',
                ],
                'libraries': [
                    '-ldl',
                ]
            }],
            ['OS=="mac"', {
                'sources': [
                    'native/src/mac-ffmpeg.c',
                ]
            }],
            ['OS=="win"', {
                'sources': [
                    'native/src/win-ffmpeg.c',
                ]
            }],
        ],
    }],
}
