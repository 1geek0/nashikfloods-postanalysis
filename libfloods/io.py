from libfloods.locations import checkPath, filecount


# Save the list of files given
def saveFiles(request, location):
    file_range = []
    x = 0
    while x < len(request.request.files['file1']):
        file = request.request.files['file1'][x]
        original_fname = file['filename']
        path = "../floodimages/" + location + '/'
        checkPath(path)
        filec = filecount(path)
        output_file = open(path + str(filec + 1) + original_fname[-4:], 'wb')
        file_range.append(str(filec + 1))
        output_file.write(file['body'])
        x += 1
    file_range = [min(file_range), max(file_range)]
    return file_range

# Gives the earliest time of given files
# def getTime(files):
#     times = []
#     for i in range(len(files)):
#         print('get time')
#         file = open(files[i], 'rb')
#         tags = exifread.process_file(file)
#         s = str(tags['EXIF DateTimeOriginal'])
#         times.append(time.mktime(datetime.datetime.strptime(s, "%Y:%m:%d %H:%M:%S").timetuple())*1000)
#     return min(times)
