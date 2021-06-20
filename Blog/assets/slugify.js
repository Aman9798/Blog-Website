const titleFiled = document.querySelector('input[name=title]');
const slugFiled = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
    .replace(/&/g,'-and-')   // replace & with and
    .replace(/[\s\W-]+/g,'-')  // replace space or mutispace with -
};

titleFiled.addEventListener('keyup', (e) => {
    slugFiled.setAttribute('value', slugify(titleFiled.value));
});