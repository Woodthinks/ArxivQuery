$(document).ready(function () {
  // 获取 popup 元素并显示
  const $popup = $('#popup');
  $popup.css('display', 'flex');

  // 获取 goToSearch 按钮并绑定点击事件
  const $goToSearchButton = $('#goToSearch');
  $goToSearchButton.on('click', function () {
    window.location.href = 'src/web/search.html';
  });
});