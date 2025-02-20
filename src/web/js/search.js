// 页面加载完成后执行代码
$(document).ready(function () {
    // 获取页面元素
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
  
    // 监听提交按钮点击事件
    $submitButton.on('click', function () {
      // 获取用户输入的值
      const title = $titleInput.val();
      const author = $authorInput.val();
      const abstract = $abstractInput.val();
      const comment = $commentInput.val();
      const journalReference = $journalReferenceInput.val();
      const subjectCategory = $subjectCategoryInput.val();
      const reportNumber = $reportNumberInput.val();
      const id = $idInput.val();
  
      // 打包成字典
      const dataDict = {
        "Title": title,
        "Author": author,
        "Abstract": abstract,
        "Comment": comment,
        "Journal Reference": journalReference,
        "Subject Category": subjectCategory,
        "Report Number": reportNumber,
        "Id": id
      };
  
      // 获取选择的规则并添加到列表中
      const rulesList = [];
      $rulesDropdown.each(function () {
        const selectedRules = $(this).find('option:selected');
        selectedRules.each(function () {
          rulesList.push($(this).val());
        });
      });
  
      // 获取max_results, download, download_path的值
      const maxResults = parseInt($maxResultsInput.val());
      const download = $downloadCheckbox.is(':checked');
      const downloadPath = $downloadPathInput.val();
  
      // 构建要发送到后端的数据对象
      const dataToSend = {
        dataDict: dataDict,
        rules: rulesList,
        max_results: maxResults,
        download: download,
        download_path: downloadPath
      };
  
      // 发送数据到后端
      $.ajax({
        url: '/search',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(dataToSend),
        dataType: 'json'
      })
      .done(function (data) {
        console.log('Success:', data);
      })
      .fail(function (error) {
        console.error('Error:', error);
      });
    });
  
    // 监听下载复选框的变化
    $downloadCheckbox.on('change', function () {
      if ($(this).is(':checked')) {
        $downloadPathInput.show();
      } else {
        $downloadPathInput.hide();
      }
    });
  });