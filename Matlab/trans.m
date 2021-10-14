function transform
    transform_list = [];
    keys = {'T', 'O', 'C', 'S', 'R'};
    values = {translate, rotate, scale, shear, reflect};
    transformations = containers.Map(keys, values);
    while True 
        transformation = input('\nEnter the transformation you want to do: \nTranslate, rOtate, sCale, Shear, Reflect \nor Done when you are done or cLear to start again: \n', 's');
        if transformation, transformaions.keys;
            transform_list = cat(1, transform_list, transformation);
        elseif strcmpi(transformation, 'd') == 1
            if size(transform_list) == 0
                disp('\nYou have entered no transformation, try again.')
                continue
            else
                break
            end
        elseif strcmpi(transformation, 'l') == 1
            transform;
        else
            disp('\nYou have entered an incorrect transformation, try again.')
            continue
        end
    end
    transform_list = transform_list';
    disp(transform_list)
    point
end

function point
    coordinates = [];
    while True
        coord = [];
        coord_in = input('\nEnter the coordinates of the shape in the format (x,y) or D when done or cLear to start again or Start again: \n');
        if strlength(coord_in) == 0
            disp('You have entered no coordinates, try again.')
            continue
        else
            if strcmpi(coord_in,'d') == 1
                if size(coordinates') == [1,1] && size(transform_list) == [1,1] && strcmpi(transform_list(1), 't') == 1 || size(coordinates) == 2 || size(coordinates) > 2
                    % do nothing
                else
                    disp('\nCannot transform a point, \nCheck transformation and points.')
                    transform
                check_coordinates
                break
                end
            elseif trcmpi(coord_in,'l') == 1
                point
            elseif trcmpi(coord_in,'s') == 1
                transform
            else
                try
                    coord_in = split(coord_in, ",");
                    coord_in = cell2mat(coord_in);
                    for c = 1:strlength(coord_in)
                        coord = cat(1, coord, str2num(coord_in(c)));
                    end
                    coord = cat(1, coord, 1);
                    coordinates = cat(1, coordinates, coord');
                catch
                    disp('An error occured with the coordinates, try again.')
                    continue
                end
            end
        end
    end
    disp(coordinates)
end

function T = translate
    return
end