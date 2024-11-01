import whisper
import time

model = whisper.load_model("turbo")

start_time= time.time()
result = model.transcribe("This_Is_Halloween_00hh_03mm_13ss.mp4")
print(result["text"])
elapsed_time = time.time() - start_time
print("--- The first transcription took %s ---" % time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))

start_time= time.time()
result = model.transcribe("This_Is_Halloween_00hh_03mm_13ss.mp4")
print(result["text"])
elapsed_time = time.time() - start_time
print("--- The second transcription took %s ---" % time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))
