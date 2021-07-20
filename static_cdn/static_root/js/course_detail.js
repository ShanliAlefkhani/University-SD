function check_chapter(chapter_id, last_chapter) {
    if (chapter_id > last_chapter) {
        document.getElementById("nextChapter").disabled = true;
    } else {
        document.getElementById("nextChapter").disabled = false;
    }
}