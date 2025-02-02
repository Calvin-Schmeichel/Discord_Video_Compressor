import ffmpeg
import os

stream = ffmpeg.input('/home/calvin/lindev/github_repos/Discord_Video_Compressor/Videos/input.mp4')
stream = ffmpeg.output(stream, 'output.mp4', video_bitrate=25000000)
ffmpeg.run(stream, overwrite_output=True)

print(os.path.getsize("/home/calvin/lindev/github_repos/Discord_Video_Compressor/output.mp4"))

# 25000000
# 62930739
#  1352084
#  8256274
# 19868619
# 39464490
 
# 6133333


'''
(bitrate/8)*seconds = 25mb
(bitrate/8) = 25mb/seconds
bitrate = (25mb/seconds)*8

6666666.66666667
6300000
'''