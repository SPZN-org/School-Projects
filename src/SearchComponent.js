import { data } from './Data';

export function searchByTitle(searchText) {
    const searchLowerCase = searchText.toLowerCase();
    return data.filter(item => item.title.toLowerCase().includes(searchLowerCase))
        .sort((a, b) => a.title.localeCompare(b.title));
}