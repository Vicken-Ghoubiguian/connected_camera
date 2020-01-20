import pyaudio
import wave

def start_recording_function(desired_format, desired_channels, desired_rate, desired_chunk):

	created_audio = pyaudio.PyAudio()

	created_stream = created_audio.open(format = desired_format, channels = desired_channels, rate = desired_rate, input = True, frames_per_buffer = desired_chunk)

	recording_frames = []

	parameters_dict = {"channels" : desired_channels, "rate" : desired_rate, "chunk" : desired_chunk, "format" : desired_format}

	return created_audio, created_stream, recording_frames, parameters_dict

def recording_function(desired_stream, recording_frames, desired_chunk):

	data = desired_stream.read(desired_chunk)

	recording_frames.append(data)

	return recording_frames

def stop_recording_function(desired_audio, desired_stream, desired_frames, desired_channels, desired_rate, desired_format):

	desired_stream.stop_stream()

	desired_stream.close()

	desired_audio.terminate()

	waveFile = wave.open("../repository_common_files/output_media_files/videos/temporary_directory/output_audio_file.wav", 'wb')

	waveFile.setnchannels(desired_channels)

	waveFile.setsampwidth(desired_audio.get_sample_size(desired_format))

	waveFile.setframerate(desired_rate)

	waveFile.writeframes(b''.join(desired_frames))

	waveFile.close()
