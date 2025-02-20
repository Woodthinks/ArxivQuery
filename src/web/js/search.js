$(document).ready(function () {

    const $keysDropdown = $('#keysDropdown');
    const $rulesDropdown = $('.rules-dropdown');
    const $titleInput = $('#titleInput');
    const $authorInput = $('#authorInput');
    const $abstractInput = $('#abstractInput');
    const $commentInput = $('#commentInput');
    const $journalReferenceInput = $('#journalReferenceInput');
    const $subjectCategoryInput = $('#subjectCategoryInput');
    const $reportNumberInput = $('#reportNumberInput');
    const $idInput = $('#idInput');
    const $maxResultsInput = $('#maxResultsInput');
    const $downloadCheckbox = $('#downloadCheckbox');
    const $downloadPathInput = $('#downloadPathInput');
    const $submitButton = $('#submitButton');
  
    const $maxResultsError = $('<span style="color: red; display: none;">This one is a must</span>');
    $maxResultsInput.after($maxResultsError);
  
    const $requiredFieldsError = $('<span style="color: red; display: none;">At least one of the previous fields must be filled</span>');
    $submitButton.before($requiredFieldsError);
  
    $rulesDropdown.on('mousedown', 'option', function(e) {
        e.preventDefault();
        const $option = $(this);
        $option.prop('selected', !$option.prop('selected'));
        $rulesDropdown.trigger('change'); 
        return false;
    });

    $submitButton.on('click', function (event) {
        if (!$maxResultsInput.val()) {
            event.preventDefault(); 
            $maxResultsError.show();
            return;
        } else {
            $maxResultsError.hide(); 
        }
  
        const title = $titleInput.val();
        const author = $authorInput.val();
        const abstract = $abstractInput.val();
        const comment = $commentInput.val();
        const journalReference = $journalReferenceInput.val();
        const subjectCategory = $subjectCategoryInput.val();
        const reportNumber = $reportNumberInput.val();
        const id = $idInput.val();
  
        if (!title && !author && !abstract && !comment && !journalReference && !subjectCategory && !reportNumber && !id) {
            event.preventDefault(); 
            $requiredFieldsError.show(); 
            return;
        } else {
            $requiredFieldsError.hide(); 
        }
  
        const prefixQueryPairs = [
            ["ti", title],
            ["au", author],
            ["abs", abstract],
            ["co", comment],
            ["jr", journalReference],
            ["cat", subjectCategory],
            ["rn", reportNumber],
            ["id", id]
        ].filter(pair => pair[1]); 
  
        const relations = [];
        $rulesDropdown.each(function () {
            const selectedRules = $(this).find('option:selected');
            selectedRules.each(function () {
                relations.push($(this).val());
            });
        });
  
        const maxResults = parseInt($maxResultsInput.val());
        const download = $downloadCheckbox.is(':checked');
        const downloadPath = $downloadPathInput.val();
  
        const dataToSend = {
            prefix_query_pairs: prefixQueryPairs,
            relations: relations,
            max_results: maxResults,
            download: download,
            download_path: downloadPath
        };
  
        $.ajax({
            url: '/search',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(dataToSend),
            dataType: 'json'
        })
        .done(function (data) {
            console.log('Success:', data);
            window.location.href = '/src/web/answer.html';
        })
        .fail(function (error) {
            console.error('Error:', error);
        });
    });
  
    $downloadCheckbox.on('change', function () {
        if ($(this).is(':checked')) {
            $downloadPathInput.show();
        } else {
            $downloadPathInput.hide();
        }
    });
});